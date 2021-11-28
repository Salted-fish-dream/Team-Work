Component({
  lifetimes: {
    created() {
      console.log("created");
    },
    attached() {
      console.log("attached");
    },
    ready() {
      console.log("ready");
    },
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
    condition: false,
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
      },
    ]
  },
  methods: {
    onChange(event) {
      wx.switchTab({
        url: this.data.list[event.detail].url
      });
    }

  }
})