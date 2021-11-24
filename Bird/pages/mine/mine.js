Component({
    pageLifetimes:{
      show:function(){
        if(typeof this.getTabBar === "function" && this.getTabBar()){
          this.getTabBar.init()
        }
      }
      
    },
    data: {
      userInfo: {},
      hasUserInfo: false,
      canIUseGetUserProfile: false,
      active: 2,
      list: [{
          text: "发现",
          icon: "home-o",
          url: "/pages/index/index"
      },
      {
          text: "看点",
          icon: "eye-o",
          url: "/pages/outcome/outcome"
      },
      {
          text: "设置",
          icon: "setting-o",
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
      console.log("load");
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
     }
   }
  })