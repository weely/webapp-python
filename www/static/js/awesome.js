// awesome.js

// patch for lower-version IE:

if (! window.console) {
    window.console = {
        log: function() {},
        info: function() {},
        error: function () {},
        warn: function () {},
        debug: function () {}
    };
}

// patch for string.trim():

if (! String.prototype.trim) {
    String.prototype.trim = function() {
        return this.replace(/^\s+|\s+$/g, '');
    };
}

if (! Number.prototype.toDateTime) {
    var replaces = {
        'yyyy': function(dt) {
            return dt.getFullYear().toString();
        },
        'yy': function(dt) {
            return (dt.getFullYear() % 100).toString();
        },
        'MM': function(dt) {
            var m = dt.getMonth() + 1;
            return m < 10 ? '0' + m : m.toString();
        },
        'M': function(dt) {
            var m = dt.getMonth() + 1;
            return m.toString();
        },
        'dd': function(dt) {
            var d = dt.getDate();
            return d < 10 ? '0' + d : d.toString();
        },
        'd': function(dt) {
            var d = dt.getDate();
            return d.toString();
        },
        'hh': function(dt) {
            var h = dt.getHours();
            return h < 10 ? '0' + h : h.toString();
        },
        'h': function(dt) {
            var h = dt.getHours();
            return h.toString();
        },
        'mm': function(dt) {
            var m = dt.getMinutes();
            return m < 10 ? '0' + m : m.toString();
        },
        'm': function(dt) {
            var m = dt.getMinutes();
            return m.toString();
        },
        'ss': function(dt) {
            var s = dt.getSeconds();
            return s < 10 ? '0' + s : s.toString();
        },
        's': function(dt) {
            var s = dt.getSeconds();
            return s.toString();
        },
        'a': function(dt) {
            var h = dt.getHours();
            return h < 12 ? 'AM' : 'PM';
        }
    };
    var token = /([a-zA-Z]+)/;
    Number.prototype.toDateTime = function(format) {
        var fmt = format || 'yyyy-MM-dd hh:mm:ss'
        var dt = new Date(this * 1000);
        var arr = fmt.split(token);
        for (var i=0; i<arr.length; i++) {
            var s = arr[i];
            if (s && s in replaces) {
                arr[i] = replaces[s](dt);
            }
        }
        return arr.join('');
    };
}

function encodeHtml(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

// parse query string as object:

function parseQueryString() {
    var
        q = location.search,
        r = {},
        i, pos, s, qs;
    if (q && q.charAt(0)==='?') {
        qs = q.substring(1).split('&');
        for (i=0; i<qs.length; i++) {
            s = qs[i];
            pos = s.indexOf('=');
            if (pos <= 0) {
                continue;
            }
            r[s.substring(0, pos)] = decodeURIComponent(s.substring(pos+1)).replace(/\+/g, ' ');
        }
    }
    return r;
}

function gotoPage(i) {
    var r = parseQueryString();
    r.page = i;
    location.assign('?' + $.param(r));
}

function refresh() {
    var
        t = new Date().getTime(),
        url = location.pathname;
    if (location.search) {
        url = url + location.search + '&t=' + t;
    }
    else {
        url = url + '?t=' + t;
    }
    location.assign(url);
}

function toSmartDate(timestamp) {
    if (typeof(timestamp)==='string') {
        timestamp = parseInt(timestamp);
    }
    if (isNaN(timestamp)) {
        return '';
    }

    var
        today = new Date(g_time),
        now = today.getTime(),
        s = '1分钟前',
        t = now - timestamp;
    if (t > 604800000) {
        // 1 week ago:
        var that = new Date(timestamp);
        var
            y = that.getFullYear(),
            m = that.getMonth() + 1,
            d = that.getDate(),
            hh = that.getHours(),
            mm = that.getMinutes();
        s = y===today.getFullYear() ? '' : y + '年';
        s = s + m + '月' + d + '日' + hh + ':' + (mm < 10 ? '0' : '') + mm;
    }
    else if (t >= 86400000) {
        // 1-6 days ago:
        s = Math.floor(t / 86400000) + '天前';
    }
    else if (t >= 3600000) {
        // 1-23 hours ago:
        s = Math.floor(t / 3600000) + '小时前';
    }
    else if (t >= 60000) {
        s = Math.floor(t / 60000) + '分钟前';
    }
    return s;
}

function getCalendar(time){
    var date = arguments[0] && arguments[0] instanceof Date ? arguments[0] : new Date(),
        year = date.getFullYear(),
        month = date.getMonth()+1,
        day = date.getDate(),
        week = date.getDay(),
        isLeap = year%4===0 && year%100!=0 || year % 4 === 0 ? true : false,
        days = month === 2 ? (isLeap ? 29 : 28) : ($.inArray(month,[1,3,5,7,8,10,12])!=-1 ? 31: 30),
        firstWeek = (week - day % 7 + 8) % 7,
        lastMonthDays = (month-1) === 2 ? (isLeap ? 29 : 28) : ($.inArray(month-1,[1,3,5,7,8,10,12])!=-1 ? 31: 30),
        calendars = new Array(),
        daylist = new Array(),
        m=0,
        n=0,
        rows = (firstWeek+days-1)%7==0 ? (firstWeek+days-1)/7+1 : (firstWeek+days-1)/7;
    for (var i=firstWeek-1;i>=0;i--){
        daylist[i] = lastMonthDays--;
    }
    for (var i=firstWeek;i<days+firstWeek;i++){
        daylist[i] = ++n;
        if (i===day+firstWeek-1){
            daylist[i] = -1;
        }
    }
    n=0;
    for (var i=0; i<rows; i++) {
        calendars[i] = new Array();
        for (var j=0; j<7; j++){
            calendars[i][j] = daylist[n] === undefined ? ++m : daylist[n];
            n++;
        }
    }
    // console.log(days+"--"+firstWeek+"-"+daylist, calendars);
    return calendars;
}

$(function() {
    $('.x-smartdate').each(function() {
        $(this).removeClass('x-smartdate').text(toSmartDate($(this).attr('date')));
    });
});


// JS Template:

function Template(tpl) {
    var
        fn,
        match,
        code = ['var r=[];\nvar _html = function (str) { return str.replace(/&/g, \'&amp;\').replace(/"/g, \'&quot;\').replace(/\'/g, \'&#39;\').replace(/</g, \'&lt;\').replace(/>/g, \'&gt;\'); };'],
        re = /\{\s*([a-zA-Z\.\_0-9()]+)(\s*\|\s*safe)?\s*\}/m,
        addLine = function (text) {
            code.push('r.push(\'' + text.replace(/\'/g, '\\\'').replace(/\n/g, '\\n').replace(/\r/g, '\\r') + '\');');
        };
    while (match = re.exec(tpl)) {
        if (match.index > 0) {
            addLine(tpl.slice(0, match.index));
        }
        if (match[2]) {
            code.push('r.push(String(this.' + match[1] + '));');
        }
        else {
            code.push('r.push(_html(String(this.' + match[1] + ')));');
        }
        tpl = tpl.substring(match.index + match[0].length);
    }
    addLine(tpl);
    code.push('return r.join(\'\');');
    fn = new Function(code.join('\n'));
    this.render = function (model) {
        return fn.apply(model);
    };
}

// extends jQuery.form:

$(function () {
    // console.log('Extends $form...');
    $.fn.extend({
        showFormError: function (err) {
            return this.each(function () {
                var
                    $form = $(this),
                    $alert = $form && $form.find('.uk-alert-danger'),
                    fieldName = err && err.data;
                if (! $form.is('form')) {
                    console.error('Cannot call showFormError() on non-form object.');
                    return;
                }
                $form.find('input').removeClass('uk-form-danger');
                $form.find('select').removeClass('uk-form-danger');
                $form.find('textarea').removeClass('uk-form-danger');
                if ($alert.length === 0) {
                    console.warn('Cannot find .uk-alert-danger element.');
                    return;
                }
                if (err) {
                    $alert.text(err.message ? err.message : (err.error ? err.error : err)).removeClass('uk-hidden').show();
                    if (($alert.offset().top - 60) < $(window).scrollTop()) {
                        $('html,body').animate({ scrollTop: $alert.offset().top - 60 });
                    }
                    if (fieldName) {
                        $form.find('[name=' + fieldName + ']').addClass('uk-form-danger');
                    }
                }
                else {
                    $alert.addClass('uk-hidden').hide();
                    $form.find('.uk-form-danger').removeClass('uk-form-danger');
                }
            });
        },
        showFormLoading: function (isLoading) {
            return this.each(function () {
                var
                    $form = $(this),
                    $submit = $form && $form.find('button[type=submit]'),
                    $buttons = $form && $form.find('button');
                    $i = $submit && $submit.find('i'),
                    iconClass = $i && $i.attr('class');
                if (! $form.is('form')) {
                    console.error('Cannot call showFormLoading() on non-form object.');
                    return;
                }
                if (!iconClass || iconClass.indexOf('uk-icon') < 0) {
                    console.warn('Icon <i class="uk-icon-*>" not found.');
                    return;
                }
                if (isLoading) {
                    $buttons.attr('disabled', 'disabled');
                    $i && $i.addClass('uk-icon-spinner').addClass('uk-icon-spin');
                }
                else {
                    $buttons.removeAttr('disabled');
                    $i && $i.removeClass('uk-icon-spinner').removeClass('uk-icon-spin');
                }
            });
        },
        postJSON: function (url, data, callback) {
            if (arguments.length===2) {
                callback = data;
                data = {};
            }
            return this.each(function () {
                var $form = $(this);
                $form.showFormError();
                $form.showFormLoading(true);
                _httpJSON('POST', url, data, function (err, r) {
                    if (err) {
                        $form.showFormError(err);
                        $form.showFormLoading(false);
                    }
                    callback && callback(err, r);
                });
            });
        }
    });
});

// ajax submit form:

function _httpJSON(method, url, data, callback) {
    var opt = {
        type: method,
        dataType: 'json'
    };
    if (method==='GET') {
        opt.url = url + '?' + data;
    }
    if (method==='POST') {
        opt.url = url;
        opt.data = JSON.stringify(data || {});
        opt.contentType = 'application/json';
    }
    $.ajax(opt).done(function (r) {
        if (r && r.error) {
            return callback(r);
        }
        return callback(null, r);
    }).fail(function (jqXHR, textStatus) {
        return callback({'error': 'http_bad_response', 'data': '' + jqXHR.status, 'message': '网络好像出问题了 (HTTP ' + jqXHR.status + ')'});
    });
}

function getJSON(url, data, callback) {
    if (arguments.length===2) {
        callback = data;
        data = {};
    }
    if (typeof (data)==='object') {
        var arr = [];
        $.each(data, function (k, v) {
            arr.push(k + '=' + encodeURIComponent(v));
        });
        data = arr.join('&');
    }
    _httpJSON('GET', url, data, callback);
}

function postJSON(url, data, callback) {
    if (arguments.length===2) {
        callback = data;
        data = {};
    }
    _httpJSON('POST', url, data, callback);
}

function postFile(method, url, data, callback){
    var opt = {
        type: method,
        dataType: 'json',
        url:  url,
        data: data,
        contentType: false,
        processData: false
    };

    $.ajax(opt).done(function (r) {
        if (r && r.error) {
            return callback(r);
        }
        return callback(null, r);
    }).fail(function (jqXHR, textStatus) {
        return callback({'error': 'http_bad_response', 'data': '' + jqXHR.status, 'message': '网络好像出问题了 (HTTP ' + jqXHR.status + ')'});
    });
}

// extends Vue:

if (typeof(Vue)!=='undefined') {
    Vue.filter('datetime', function (value) {
        var d = value;
        if (typeof(value)==='number') {
            d = new Date(value);
        }
        return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate() + ' ' + d.getHours() + ':' + d.getMinutes();
    });
    Vue.component('pagination', {
        props:{
            has_previous:Boolean,
            has_next: Boolean,
            page_index: Number,
            page_count: Number
        },
        template: '<div><ul class="uk-pagination uk-pagination-right">' +
                '<li v-if="! has_previous" class="uk-disabled"><span><i class="uk-icon-angle-double-left"></i></span></li>' +
                '<li v-if="has_previous"><a v-on:click="gotoPage(page_index-1)" href="#0"><i class="uk-icon-angle-double-left"></i></a></li>' +
            '<template v-if="page_count<=5">'+
                '<li v-for="n in (page_count)" v-if="n !== page_index"><a v-on:click="gotoPage(n)">{{n}}</a></li>' +
                '<li v-else-if="n === page_index" class="uk-active"><span v-text="page_index"></span></li>' +
            '</template>' +
            '<template v-else-if="page_count>5">' +
                '<template v-if="page_index<=4">' +
                    '<li v-for="n in 5" v-if="n !== page_index"><a v-on:click="gotoPage(n)">{{n}}</a></li>' +
                    '<li v-else-if="n === page_index" class="uk-active"><span v-text="page_index"></span></li>' +
                    '<li ><span>...</span></li>' +
                '</template>' +
                '<template v-else-if="(page_index + 4) < page_count">' +
                    '<li><span>...</span></li>' +
                    '<li v-for="n in (page_index + 2)" v-if="n > page_index-3 && n !== page_index"><a v-on:click="gotoPage(n)">{{n}}</span></a></li>' +
                    '<li v-else-if="n === page_index" class="uk-active"><span v-text="page_index"></span></li>' +
                    '<li><span>...</span></li>' +
                '</template>' +
                '<template v-else-if="(page_index + 4) >= page_count">' +
                    '<li ><span>...</span></li>' +
                    '<li v-for="n in page_count" v-if="n !== page_index && n>page_count-5"><a v-on:click="gotoPage(n)">{{n}}</a></li>' +
                    '<li v-else-if="n === page_index" class="uk-active"><span v-text="page_index"></span></li>' +
                '</template>' +
            '</template>' +
                '<li v-if="! has_next" class="uk-disabled"><span><i class="uk-icon-angle-double-right"></i></span></li>' +
                '<li v-if="has_next"><a v-on:click="gotoPage(page_index+1)" href="#0"><i class="uk-icon-angle-double-right"></i></a></li>' +
            '</ul></div>',
        methods: {
            gotoPage: function(i){
                var r = parseQueryString();
                r.page = i;
                location.assign('?' + $.param(r))
            }
        }
    });
    Vue.component('calendar', {
        template: '<div>'+
                '<table class="uk-table calendar" title="calendar">' +
                    '<thead>' +
                        '<tr><th><div><a @click="pre_month" href="#0"><i class="uk-icon-arrow-left"></i></a></div></th>' +
                        '<th colspan="5">{{ year + "年" + (month+1) + "月"}}</th>' +
                        '<th><div><a @click="next_month" href="#0"><i class="uk-icon-arrow-right "></i></a></div></th></tr>' +
                        '<tr><th v-for="w in weeks">{{ w }}</th></tr>' +
                    '</thead>' +
                    '<tbody>'+
                        '<tr v-for="rows in calendar">' +
                            '<td v-for="item in rows" v-if="item === -1" style="text-decoration:underline;color: blue;"><i>{{ date }}</i></td>' +
                            '<td v-else>{{ item }}</td>' +
                        '</tr>' +
                    '</tbody>' +
                '</table>' +
            '</div>',
        data: function(){
            var today = new Date();
            return {
                weeks: ['日', '一', '二', '三', '四', '五', '六'],
                year: today.getFullYear(),
                month: today.getMonth(),
                date: today.getDate(),
                week: today.getDay(),
                calendar: getCalendar()
            }
        },
        methods: {
            pre_month: function(){
                var today = new Date();
                this.year = this.month == 0 ? this.year-1 : this.year;
                this.month = this.month == 0 ? 11 : this.month-1;
                this.date = this.year===today.getFullYear() && this.month === today.getMonth() ? today.getDate() : 1;
                this.calendar = getCalendar(new Date(this.year,this.month,this.date));
                console.log(this.calendar)
            },
            next_month: function(){
                var today = new Date();
                this.year = this.month == 11 ? this.year+1 : this.year;
                this.month = this.month == 11 ? 0 : this.month+1;
                this.date = this.year===today.getFullYear() && this.month === today.getMonth() ? today.getDate() : 1;
                this.calendar = getCalendar(new Date(this.year,this.month,this.date));
            }
        }
    });
}

function redirect(url) {
    var
        hash_pos = url.indexOf('#'),
        query_pos = url.indexOf('?'),
        hash = '';
    if (hash_pos >=0 ) {
        hash = url.substring(hash_pos);
        url = url.substring(0, hash_pos);
    }
    url = url + (query_pos >= 0 ? '&' : '?') + 't=' + new Date().getTime() + hash;
    console.log('redirect to: ' + url);
    location.assign(url);
}

// init:

function _bindSubmit($form) {
    $form.submit(function (event) {
        event.preventDefault();
        showFormError($form, null);
        var
            fn_error = $form.attr('fn-error'),
            fn_success = $form.attr('fn-success'),
            fn_data = $form.attr('fn-data'),
            data = fn_data ? window[fn_data]($form) : $form.serialize();
        var
            $submit = $form.find('button[type=submit]'),
            $i = $submit.find('i'),
            iconClass = $i.attr('class');
        if (!iconClass || iconClass.indexOf('uk-icon') < 0) {
            $i = undefined;
        }
        $submit.attr('disabled', 'disabled');
        $i && $i.addClass('uk-icon-spinner').addClass('uk-icon-spin');
        postJSON($form.attr('action-url'), data, function (err, result) {
            $i && $i.removeClass('uk-icon-spinner').removeClass('uk-icon-spin');
            if (err) {
                console.log('postJSON failed: ' + JSON.stringify(err));
                $submit.removeAttr('disabled');
                fn_error ? fn_error() : showFormError($form, err);
            }
            else {
                var r = fn_success ? window[fn_success](result) : false;
                if (r===false) {
                    $submit.removeAttr('disabled');
                }
            }
        });
    });
    $form.find('button[type=submit]').removeAttr('disabled');
}

$(function () {
    $('form').each(function () {
        var $form = $(this);
        if ($form.attr('action-url')) {
            _bindSubmit($form);
        }
    });
});

$(function() {
    if (location.pathname === '/' || location.pathname.indexOf('/blog')===0) {
        $('li[data-url=blogs]').addClass('uk-active');
    }
});

function _display_error($obj, err) {
    if ($obj.is(':visible')) {
        $obj.hide();
    }
    var msg = err.message || String(err);
    var L = ['<div class="uk-alert uk-alert-danger">'];
    L.push('<p>Error: ');
    L.push(msg);
    L.push('</p><p>Code: ');
    L.push(err.error || '500');
    L.push('</p></div>');
    $obj.html(L.join('')).slideDown();
}

function error(err) {
    _display_error($('#error'), err);
}

function fatal(err) {
    _display_error($('#loading'), err);
}
