import Dialog from "../../miniprogram_npm/@vant/weapp/dialog/dialog";
import Notify from "../../miniprogram_npm/@vant/weapp/notify/notify";
import Toast from "../../miniprogram_npm/@vant/weapp/toast/toast";
Component({
  lifetimes: {
    created() {
     
    },
    attached() {
  
    }
  },
  pageLifetimes: {
    show() {
      if (typeof this.getTabBar === "function" && this.getTabBar()) {
        this.getTabBar.init()
      }
    },
  },
  data: {
    active: 1,
    getUploadFile: "",
    condition: true,
    extraContent: "   ",
    name: "",
    BirdInfo : "",
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
      },
    ]
  },
  methods: {

    showTips(){
      Toast('已经到底了');
    },

    changeFlag(){
      var that = this
      wx.getStorage({
        key: "BirdInfo",
        success(res){
          console.log(res)
          that.setData({
            BirdInfo: res.data.bird_msg,
            name:res.data.bird_name,
            condition:false
          })
        },fail(res){
          wx.showToast({
            title: '未收录这个品种',
            icon: 'error',
            duration: 2000,
            mask: true
          })
        }
      }),
      wx.getStorage({
        key: "openid",
        success(res){
        },fail(res){
          console.log("无id");
          wx.showToast({
            title: '请先进行验证',
            icon: 'error',
            duration: 2000,
            mask: true
          })
        }
      })
    },

    onChange(event) {
      wx.switchTab({
        url: this.data.list[event.detail].url
      });

    },
    isDelete(){
      var that = this
      Dialog.confirm({
        title: "",
        message: "你确定要删除这项记录吗",
      }).then(()=> {
        // on confirm
        Notify({ type:'success', message: '删除成功'})
        wx.removeStorage({
          key: 'uploadFile',
          success (res){
            that.setData({
              condition: true
            })
          }
        }),
        wx.removeStorage({
          key: 'BirdInfo'
        })
      })
      .catch(()=>{
        // on cancel
        Notify({ type:'warning', message: '删除取消'})
      })
    }

  }
})