$(function(){
    // 判断低版本的IE浏览器
    function myBrowser(){
        var userAgent = navigator.userAgent;
        var isOpera = userAgent.indexOf("Opera") > -1;
        var isIE = userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1 && !isOpera;
        if (isIE) {
            var IE5 = IE55 = IE6 = IE7 = IE8 = false;
            var reIE = new RegExp("MSIE (\\d+\\.\\d+);");
            reIE.test(userAgent);
            var fIEVersion = parseFloat(RegExp["$1"]);
            IE55 = fIEVersion == 5.5;
            IE6 = fIEVersion == 6.0;
            IE7 = fIEVersion == 7.0;
            IE8 = fIEVersion == 8.0;
            if (IE55 || IE6 || IE7 || IE8) {
                return "lowVersionIE";
            }
        }
    }
    if (myBrowser() == "lowVersionIE") {
        var lowVersionTip = document.createElement("div");
        lowVersionTip.id = "LVTips";
        lowVersionTip.innerText = "温馨提示：不支持IE8及以下浏览器，为了保证最佳使用体验，请升级您的浏览器！";
        document.body.appendChild(lowVersionTip);
    }

    $('.login-form').validate({
        errorElement: 'span', //default input error message container
        errorClass: 'help-block', // default input error message class
        focusInvalid: false,
        onsubmit:true,// 是否在提交是验证
        onfocusout:false,// 是否在获取焦点时验证
        onkeyup :false,// 是否在敲击键盘时验证 
         // do not focus the last invalid input
        rules: {
            username: {
                required: true
            },
            password: {
                required: true
            },
            remember: {
                required: false
            }
        },

        messages: {
            username: {
                required: "用户名是必填的."
            },
            password: {
                required: "密码是必填的."
            }
        },

        invalidHandler: function(event, validator) { //display error alert on form submit
            $("#error_message").html("用户名或密码错误");
            $('.alert-danger', $('.login-form')).show();

        },

        highlight: function(element) { // hightlight error inputs
            $(element).closest('.form-group').addClass('has-error'); // set error class to the control group
        
        },

        success: function(label) {
            label.closest('.form-group').removeClass('has-error');
            label.remove();
        },

        errorPlacement: function(error, element) {
            error.insertAfter(element.closest('.input-icon'));
        },
        submitHandler: function(form) {
            
            $.ajax({
                type: "POST",
                async : true,
                cache : true,
                dataType : "json",
                url:"login",
                data:$(".login-form").serialize(),
                error:function(){
                    console.log("login/error")
                },
                success:function(data){
                    if(data.code==101){
                        $("#error_message").html(data.message);
                        $('.alert-danger', $('.login-form')).show();
                    }else if(data.code==201){
                        var user_name=data.result.user_name;
                        setCookie('user_name',user_name);
                        var avatar=data.result.avatar;
                        var user_role=data.result.user_role;
                        setCookie('user_role',user_role);
                        window.location.href="dashboard.html";
                    }
                }
            })
        },
        
    });
    $('.login-form input').keypress(function(e) {
        if (e.which == 13) {
            if ($('.login-form').validate().form()) {
                $('.login-form').submit(); //form validation success, call ajax form submit
            }
            return false;
        }
    });
    // 兼容属性 placeholder
    if(!isSupportPlaceholder()) {
        $('input[type="text"]').each(
            function() {
                var self = $(this);
                var val = self.attr("placeholder");
                input(self, val);
            }
        );
        $('input[type="password"]').each(
            function() {
                var pwdField = $(this);
                var pwdVal = pwdField.attr('placeholder');
                var pwdId = pwdField.attr('id');
                // 重命名该input的id为原id后跟1
                pwdField.after('<input id="' + pwdId + '1" class="form-control form-control-solid placeholder-no-fix required" type="text" value='+pwdVal+' autocomplete="off"/>');
                var pwdPlaceholder = $('#' + pwdId + '1');
                pwdPlaceholder.show();
                pwdField.hide();

                pwdPlaceholder.focus(function(){
                    pwdPlaceholder.hide();
                    pwdField.show();
                    pwdField.focus();
                });
                pwdField.blur(function(){
                    if(pwdField.val() == '') {
                        pwdPlaceholder.show();
                        pwdField.hide();
                    }
                });
            }
        );
    }
    function isSupportPlaceholder() {
        var input = document.createElement('input');
        return 'placeholder' in input;
    }
    function input(obj, val) {
        var $input = obj;
        var val = val;
        $input.attr({value:val});
        $input.focus(function() {
            if ($input.val() == val) {
                $(this).attr({value:""});
            }
        }).blur(function() {
            if ($input.val() == "") {
                $(this).attr({value:val});
            }
        });
    }
})