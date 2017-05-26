/*登录校验*/
function check_login(){
    var user_name = $("#username").val();
    var password = $("#password").val();

    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/login",
        data: {
            "user_name": user_name,
            "password": password
        },
        error: function(){
            console.log("/login/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                var username=data.result.username;
                setCookie('user_name',username);

                var user_role=data.result.user_role;
                setCookie('user_role',user_role);
                window.location.href="index.html";
            }
        }
    });
}