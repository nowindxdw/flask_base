$(function () {
    nav_top_menu();
});

//主菜单单击处理
function nav_top_menu() {
    $("#nav_top_menu a, #nav_userinfo a").click(function (e) {
        var url = $(this).attr("href");
        GLOBALURL = url;
        if (url == "javascript:;" || url == "#" || url == "") {
            return true
        }
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: url,
            // SELECTEDTREEID defined in app.js
            data: {"nodeid": SELECTEDTREEID},
            dataType: "html",
            success: function (result) {
                $('#qmain-content').html(result);
            },
            error: function () {
                alert("请求失败，请稍候再试");
            }
        });
    });
}


