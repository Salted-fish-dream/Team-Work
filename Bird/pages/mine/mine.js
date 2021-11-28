Component({
    lifetimes:{
      attached() {
        var that = this
        wx.getStorage({
          key: "openid",
          success(res){
            // console.log(res.data);
            that.setData({
              openID: res.data
            })
          }
        
        })
      }
    },
    pageLifetimes:{
      show:function(){
        if(typeof this.getTabBar === "function" && this.getTabBar()){
          this.getTabBar.init()
        }
      }
      
    },
    data: {
      motto: '欢迎使用鸟类识别小程序',
      userInfo: {},
      openID:"",
      hasUserInfo: false,
      canIUseGetUserProfile: false,
      active: 2,
      list: [{
          text: "发现",
          icon: "home-o",
          url: "/pages/index/index"
      },
      {
          text: "结果",
          icon: "eye-o",
          url: "/pages/outcome/outcome"
      },
      {
          text: "我的",
          icon: "user-o",
          url: "/pages/mine/mine"
      },]
    },
   methods:{
     onChange(event) {
      wx.switchTab({
        url: this.data.list[event.detail].url
      });
     },
     onLoad:function(){
       var that = this
      if(wx.getUserProfile){
        this.setData({
          canIUseGetUserProfile: true
        })
      }
     },
     getUserProfile(e){
       wx.getUserProfile({
         desc: '占位',
         success:(res) => {
           this.setData({
             userInfo:res.userInfo,
             hasUserInfo:true
           })
         }
       })
       wx.login({
        success: res => {
          console.log("调用成功");
          // 发送 res.code 到后台换取 openId, sessionKey, unionId
          if(res.code){
              wx.request({
                url: 'http://120.55.13.233:8001/login/',
                data: {
                  code:res.code
                },
                success:function(res){
                  console.log(res.data.data.token)
                  wx.setStorage({
                    key: "openid",
                    data: res.data.data.token
                  })
                }
              })
          } else{
            console.log("登陆失败" + res.errMsg);
          }
        }
      })
     },
    //  getRecord(){
    //    var that = this
    //     wx.request({
    //       url: 'http://120.55.13.233:8001/history',
    //       data:{
    //         openid: that.data.openID
    //       },
    //       method : "GET",
    //       success:function(res){
    //         console.log(res);
    //         var response = JSON.parse(res.data)
    //       }
    //     })
    //  }
   }
  })