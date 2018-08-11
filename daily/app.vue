<template>
    <div class="daily">
        <div class="daily-menu">
            <div class="daily-menu-item" :class="{ on: type === 'recommend'}" @click="handleToRecommend">每日推荐</div>
            <div class="daily-menu-item" :class="{ on: type === 'daily'}" @click="showThemes = !showThemes">主题日报</div>
            <ul v-show="showThemes">
                <li v-for="item in themes">
                    <a :class="{on:item.id===themeId && type === 'daily'}"
                    @click="handleToTheme(item.id)">{{ item.name }}</a>
                </li>
            </ul>
        </div>
        <div class="daily-list">
            <template v-if="type === 'recommend'">
                <div v-for="list in recommendList">
                    <div class="daily-date">{{ formatDay(list.date) }}</div>
                    <Item v-for="item in list.stories" :data="item"></Item>
                </div>
            </template>
            <template v-if="type==='daily'">
                <Item v-for="item in list" :data="item" :key="item.id"></Item>
            </template>
        </div>
        <!-- <daily-article></daily-article> -->
    </div>
</template>

<script>
import $ from './libs/util.js'
import axios from 'axios'
import Item from './components/item.vue'
export default {
    components:{Item},
    data () {
        return {
            themes: [],
            showThemes: false,
            type: 'recommand',
            list:[],
            recommendList:[],
            themeId: 0,
            dailyTime: $.getTodayTime(),
            isLoading: false
        }
    },
    methods:{
        getThemes(){
            $.ajax.get('themes/').then(res=>{
                this.themes = res.others;
            })
            // axios({
            //     method:"get",
            //     url: 'http://127.0.0.1:8000/api/themes'
            // }).then((res)=>{
            //     this.themes = res.others;
            // })
        },
        handleToTheme(id){
            this.type = 'daily';
            this.themeId = id;
            this.list = [];
            $.ajax.get('theme/'+id+'/').then(res => {
                this.list = res.stories.filter(item => item.type !== 1);
            })
        },
        handleToRecommend(){
            this.type = 'recommend',
            this.recommendList = [],
            this.dailyTime = $.getTodayTime();
            this.getRecommendList();
        },
        getRecommendList(){
            this.isLoading = true;
            const prevDay = $.prevDay(this.dailyTime + 86400000);
            $.ajax.get('news/before/'+prevDay).then(res=>{
                this.recommendList.push(res);
                this.isLoading=false;
            })
        },
        formatDay(date){
            let month = date.substr(4,2);
            let day = date.substr(6,2);
            if (month.substr(0,1) ==='0') month = month.substr(1,1);
            if (day.substr(0,1) ==='0') day =day.substr(1,1);
            return month+'月'+day+'日';
        }
    },
    mounted(){
        this.handleToRecommend();
        this.getThemes();
    }
}
</script>

<style>

</style>