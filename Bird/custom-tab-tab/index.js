Component({
    data: {
        active: '',
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

    methods: {
        onChange(event){
            wx.switchTab({
              url: this.data.list[event.detail].url,
            });
        },
        init(){
            const page = getCurrentPages().pop();
            this.setData({
                active: this.data.list.findIndex(item => item.url === `/${page.route}`)
            })
        }
    }
})