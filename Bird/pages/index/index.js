const app = getApp()
var that
var util = require('../../utils/util.js')
Page({
  /**
   * 页面的初始数据
   */
  data: {
    active:0,
    getTestImg: '../../resources/image/003.jpg',
    files: [], // 图片文件数组
    urls: [], // 内容URL地址数组
    time:null, // 装饰用时间
    list: [{
      text: "发现",
      icon: "home-o",
      url: "/pages/index/index", 
  },{
      text: "看点",
      icon: "eye-o",
      url: "/pages/outcome/outcome",
  },{
      text: "设置",
      icon: "setting-o",
      url: "/pages/mine/mine", 
  }]
  },

  onChange(e){
    var i = e.detail;
    wx.switchTab({
      url: this.data.list[i].url,
    })
    this.setData({
      chosenIndex : i
    })
   
  },

  /**
   * 拍照进行处理函数
   */
  bindUpload: function () {
    var that = this
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['camera'],
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        var tempFilePaths = res.tempFilePaths
        console.log(tempFilePaths[0])
        wx.uploadFile({
          filePath: 'tempFilePaths[0]',
          name: 'uploadFile', // 文件对应的键名，后端可以通过这个key获取到文件的二进制内容
          url: 'url',
          formDta: {
            'user_id': '123',
          },
          success: function (res) {
            var object = res
            wx.setStorage({
              key: "imgPath",
              data: object
            }, {
              key: "text",
              data: object
            })

          }
        })
      }
    })
  },

  /**
   * 选择图片进行处理函数
   */
  bindUpload1: function () {
    var that = this
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['album'],
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        var tempFilePaths = res.tempFilePaths
        console.log(tempFilePaths[0])
        wx.uploadFile({
          filePath: 'tempFilePaths[0]',
          name: 'uploadFile', // 文件对应的键名，后端可以通过这个key获取到文件的二进制内容
          url: 'url',
          formDta: {
            'user_id': '123',
          },
          success: function (res) {
            var object = res
            wx.setStorage({
              key: "imgPath",
              data: object
            }, {
              key: "text",
              data: object
            })

          }
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // 调用函数时，传入new Date()参数，返回值是日期和时间
    var time = util.formatDate(new Date());
    this.setData({
      time:time
    })
    console.log()
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
      
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})