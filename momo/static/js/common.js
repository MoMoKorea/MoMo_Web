    baseUrl = "http://" + $(location).attr('host') + "/"
    axios.defaults.headers.baseURL = baseUrl
    axios.defaults.headers.post['X-CSRFToken'] = $("[name=csrfmiddlewaretoken]").val()
    Vue.prototype.$http = axios


    /**
     * 문자열이 빈 문자열인지 체크하여 결과값을 리턴한다.
     * @param str       : 체크할 문자열
     */
    function isEmpty(str){

        if(typeof str == "undefined" || str == null || str == "")
            return true;
        else
            return false ;
    }

    /**
     * 문자열이 빈 문자열인지 체크하여 기본 문자열로 리턴한다.
     * @param str           : 체크할 문자열
     * @param defaultStr    : 문자열이 비어있을경우 리턴할 기본 문자열
     */
    function nvl(str, defaultStr){

        if(typeof str == "undefined" || str == null || str == "")
            str = defaultStr ;

        return str ;
    }


    // 금액 천단위마다 콤마(,) 추가
    function numberWithCommas(price) {
        return String(price).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }




