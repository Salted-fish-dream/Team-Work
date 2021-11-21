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
     }
   }
  })