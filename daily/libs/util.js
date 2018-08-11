import axios from 'axios'

// const axios = require('axios')

const Util = {
    apiPath: 'http://127.0.0.1:8000/api/',
    // imgPath: ''
}

Util.ajax = axios.create({
    baseURL: Util.apiPath
})

Util.ajax.interceptors.response.use(res => {
    return res.data
})

// Util.ajax('themes').then(res=>{
//     console.log(res.others)
// })

Util.getTodayTime = function () {
    const date = new Date();
    date.setHours(0);
    date.setMinutes(0);
    date.setSeconds(0);
    date.getMilliseconds(0);
    return date.getTime()
};

Util.prevDay = function (timestamp = (new Date()).getTime()) {
    const date = new Date(timestamp);
    const year = date.getFullYear();
    const month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1;
    const day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate();
    return year+month+day;

};

export default Util