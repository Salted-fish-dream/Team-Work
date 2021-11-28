// app.js
App({
  onLaunch() {
  
    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        if(res.code){
            wx.request({
              url: 'url',
              data: {
                code:res.code
              }
            })
        } else{
          console.log("登陆失败" + res.errMsg);
        }
        
      }
    })
  },
  globalData: {
    userInfo: null,
    code: {
      // 操作成功
      SUCCESS: 200,
      // 操作失败
      FAIL: 500
    }
  }
})
