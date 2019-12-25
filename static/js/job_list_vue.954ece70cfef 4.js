


var listVue = new Vue({
    el: '#content',
    delimiters: ['[[', ']]'],
    data: {
        totalPage: 1,
        currentPage: 1,
        jobList: []
    },
    methods: {

        onLoadMoreScroll: function() {

            var totalPage = this.totalPage
            var currentPage = this.currentPage

            var windowHeight = $(window).height();
            $(window).scroll(function () {

                var documentHeight = $(document).height();
                var scrollHeight = documentHeight - windowHeight

                if (scrollHeight > 200) {
//
                   var scrollY = $(document).scrollTop();
                   if (scrollY > (scrollHeight - 200)) {
                        // 페이징을 호출한다.
                        
                   }
               }
            });

        }

    },
    mounted () {
        this.onLoadMoreScroll()
    }



})