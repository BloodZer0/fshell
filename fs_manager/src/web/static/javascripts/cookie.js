function getCookie(cookie_name) {
	if (document.cookie.length>0) {
		cookie_start=document.cookie.indexOf(cookie_name + "=");
		if (cookie_start!=-1)
		{
			cookie_start=cookie_start + cookie_name.length+1;
			cookie_end=document.cookie.indexOf(";",cookie_start);
			if (cookie_end==-1) cookie_end=document.cookie.length;
			return unescape(document.cookie.substring(cookie_start,cookie_end))
		}
	}
	return ""
}

function deleteCookie(cookie_name) {
	var exp = new Date();
	exp.setTime(exp.getTime() - 1);
	var cval = getCookie(cookie_name);
	document.cookie = cookie_name + "=" + cval + "; path=/ ;expires=" + exp.toGMTString();
}

function setCookie(cookie_name,value,expiredays) {
	var exdate=new Date();
	exdate.setDate(exdate.getDate()+expiredays);
	document.cookie=cookie_name+ "=" +escape(value)+
		((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
}

/*
function checkCookie() {
	//用户名
	user_name=getCookie('user_name');
	if (user_name!=null && user_name!="") {
		$("#user_name").html( user_name )
	}

	//用户角色
	user_role=getCookie('user_role');
	if (user_role!=null && user_role!="") {
		if(user_role==0){
			$("#user_avatar").attr("src","../static/image/sup_user_sm.jpg" )
		}else if(user_role==1){
			$("#user_avatar").attr("src","../static/image/sup_user_sm.jpg" );
			$("#log_manage").remove();
		}else if(user_role==2){
			$("#user_avatar").attr("src","../static/image/user_sm.jpg" );
			$("#log_manage").remove();
		}
	}
}
*/