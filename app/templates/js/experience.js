$(document).ready(function() {
    initialize_page();
    get_tag_list(3);
    get_experiences_list(1);
    set_copyright_version();

    // 点赞
    $("#user_likes").click(function() {
        is_need_login();

        var user_like_status = 1; // 0点赞，1取消
        if ($("#user_likes").attr("style") != "color:#f7726b") {
            user_like_status = 0;
        }
        var datas = get_json({ 'ctype': 3, 'status': user_like_status, 'gid': experience_id })
        $.ajax({
            type: 'post',
            url: get_url("/userfellgoods"),
            headers: get_headers(),
            data: datas,
            xhrFields: { withCredentials: true },
            crossDomain: true,
            success: function(str) { //返回json结果
                if (str.status == 200) {
                    // 评论成功, 局部刷新评论内容
                    // 点赞成功
                    if (user_like_status == 0) {
                        $("#user_likes").attr("style", "color:#f7726b");
                        $('#experience_likes').text(Number($('#experience_likes').text()) + 1);
                        // 点赞失败
                    } else {
                        $("#user_likes").attr("style", "");
                        $('#experience_likes').text(Number($('#experience_likes').text()) - 1);
                    }

                } else {
                    alert(str.msg);
                    remove_user_login_status(str.msg);
                }

            },
            fail: function(err, status) {
                alert(err.data);
                console.log(err);
            }
        });
    });

    // 收藏
    $("#user_collectons").click(function() {
        is_need_login();

        var user_like_status = 1; // 0点赞，1取消
        if ($("#user_collectons").attr("style") != "color:#f7726b") {
            user_like_status = 0; // 未点赞
        }
        var datas = get_json({ 'ctype': 3, 'status': user_like_status, 'cid': experience_id })
        $.ajax({
            type: 'post',
            url: get_url("/usercollections"),
            headers: get_headers(),
            data: datas,
            xhrFields: { withCredentials: true },
            crossDomain: true,
            success: function(str) { //返回json结果
                if (user_like_status == 0) {
                    $("#user_collectons").attr("style", "color:#f7726b");
                    $('#experience_collectons').text(Number($('#experience_collectons').text()) + 1);
                    // 点赞失败
                } else {
                    $("#user_collectons").attr("style", "");
                    $('#experience_collectons').text(Number($('#experience_collectons').text()) - 1);
                }
            },
            fail: function(err, status) {
                alert(err.data);
                console.log(err);
            }
        });
    });

});

//获取标签列表
function get_tag_list(type){
    $.ajax(
        {
            type:'get',
            url:get_url("/gettaglist?type=" + type),
            success:function(str){//返回json结果
                if (str.status == 200) {
                    var content = "";
                    var data = str.data[0].tags;
                    var tags = data.split(",");
                    for (var i = 0; i < tags.length; i++){
                        var tag = "<div class=\"meaus-item\">"+tags[i]+"</div>";
                        content = content + tag;
                    }
                    $("#meaus").append(content);
                }

            },
            fail: function(err, status) {
                alert("数据获取失败！");
                console.log(err);
        }}
    );
    
}


// 获取问题列表
function get_experiences_list(nums) {
    $.ajax({
        type: 'get',
        url: get_url("/getarticle?pagenum=" + nums),
        success: function(str) { //返回json结果
            if (str.status == 200) {
                // 获取成功
                var c = '';
                var content = '';
                var datas = str.data.contentlist
                var counts = str.data.counts
                for (var i = 0; i < datas.length; i++) {
                    var author_id = datas[i].uid;
                    var author_name = datas[i].nickname
                    var author_headpic = get_img_url(datas[i].headpic)
                    var author_infomation = datas[i].userinfo

                    var experience_reading = 456; // 阅读量
                    var experience_comments = 456; // 评论量
                    var experience_likes = datas[i].goods; // 点赞数
                    var experience_collectons = datas[i].collections; // 收藏量

                    var experience_id = datas[i].id; // 文章id
                    var experience_title = datas[i].title; // 标题
                    var experience_content = datas[i].brief; // 内容
                    var experience_creattime = datas[i].times; // 创建时间
                    var experience_imag_url = get_img_url(datas[i].ximg); // 文章图片

                    c = '<div class="list-item" onclick="go_experience_details(' + experience_id + ')"   style="cursor:pointer;">' +
                        '<p class="list-item-title" style="word-break:break-all;">' + experience_title + '</p>' +
                        '<div class="user-box">' +
                        '<div class="img-box">' +
                        '<img src="' + author_headpic + '" alt="" onclick="go_personal_center(' + author_id + ')" style="cursor:pointer;"/>' +
                        '</div>' +
                        '<div class="info">' +
                        '<p class="name" onclick="go_personal_center(' + author_id + ')" style="cursor:pointer;">' + author_name + '</p>' +
                        '<p class="job">' + author_infomation + '</p>' +
                        ' </div>' +
                        '</div>' +
                        '<div class="infos">' +
                        '<div class="img-box">' +
                        '<img src="' + experience_imag_url + '" alt="" />' +
                        '</div>' +
                        '<div class="desc" >' +
                        '<p class="desc-word" style="word-break:break-all;">' + experience_content + '</p>' +
                        '<a href="javascript:go_experience_details(' + experience_id + ')" class="more">' +
                        // '<label class="cf7">[...查看详情]</label>' +
                        '</a>' +
                        '</div>' +
                        '</div>' +
                        '<div class="other">' +
                        '<span class="other-item date">' + experience_creattime + '</span>' +
                        // '<div class="other-item other-icon">' +
                        // '<span class="glyphicon glyphicon-comment"></span>' +
                        // '<span>评论' + experience_comments + '</span>' +
                        // '</div>' +
                        // '<div class="other-item other-icon">' +
                        // '<span class="glyphicon glyphicon-open"></span>' +
                        // '<span>阅读' + experience_reading + '</span>' +
                        // '</div>' +
                        '<div class="other-item other-icon">' +
                        '<span class="glyphicon glyphicon-user" id="user_likes"></span>' +
                        '<span>点赞' + experience_likes + '</span>' +
                        '</div>' +
                        '<div class="other-item other-icon">' +
                        '<span class="glyphicon glyphicon-heart" id="user_collectons"></span>' +
                        '<span>收藏' + experience_collectons + '</span>' +
                        '</div>' +
                        '</div>' +
                        '</div>'

                    content = content + c;
                }
                $('#experience_list').html(content);

                // 分页相关
                $('#total').val(counts);
                compute_pagenum(nums, "get_experiences_list", -10000)

            } else {
                alert("数据获取失败！");
                remove_user_login_status(str.msg)

            }

        },
        fail: function(err, status) {
            alert("数据获取失败！");
            console.log(err);
        }
    });
}


// 是否显示回复框
function show_repeat_div(id) {
    var status = $("#q" + id).css('display');
    if (status == 'none') {
        $("#q" + id).show();
    } else {
        $("#q" + id).hide();
    }
}

// 回复问题
function repeat_experience(id) {
    is_need_login();

    var experience_id = id;
    var repeat_content = $("#q" + experience_id).val();
    is_content_not_null(repeat_content);
    var datas = get_json({ "ctype": 1, "comment": repeat_content, "fid": experience_id });
    $.ajax({
        type: 'post',
        url: get_url("/comment/new"),
        headers: get_headers(),
        data: datas,
        xhrFields: { withCredentials: true },
        crossDomain: true,
        success: function(str) { //返回json结果
            if (str.status == 200) {
                // 回复成功
                alert("评论成功")
                go_experience_details(experience_id)
            } else {
                alert(str.msg);
                remove_user_login_status(str.msg)

            }

        },
        fail: function(err, status) {
            alert(err.data);
            console.log(err);
        }
    });
}