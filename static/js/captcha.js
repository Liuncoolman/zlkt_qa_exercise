$(function () {
  var nums = 5;
  var clock;
  $('#captcha').on('click', () => {
    // 获取email
    var email = $('#email').val()
    if (email) {
      $.ajax({
        url: `/user/get_captcha?email=${email}`,
        method: 'GET',
        success: (res) => {
          if (res.code === 0) {
            $('#captcha').text(nums + '秒可后重新获取')
            $('#captcha').attr("disabled", "true");//将按钮置为不可点击
            clock = setInterval(doLoop, 1000); //一秒执行一次
            alert(res.msg)
          }
        }
      })
    } else {
      alert('请先输入邮箱')
    }
  })

  function doLoop() {
    nums--;
    if (nums > 0) {
      $('#captcha').text(nums + '秒后可重新获取');
    } else {
      clearInterval(clock); //清除js定时器
      $('#captcha').removeAttr("disabled");
      $('#captcha').text('验证码');
      nums = 60; //重置时间
    }
  }

})