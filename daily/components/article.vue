<template>
    <div class="daily-article">
        <div class="daily-article-title">{{ data.title }}</div>
        <div v-html="data.body" class="daily-article-content"></div>
    </div>
</template>

<script>
import $ from '../libs/util';
export default {
    props:{
        articleId :{
            type:[String, Number]
        }
    },
    data(){
        return {
            data: {}
        }
    },
    watch:{
        articleId: function(){
            try{
                $.ajax.get('news/'+this.articleId).then(res=>{
                    res.body = res.body.replace(/src="http:/g, 'src="'+ $.apiPath + 'img?img=http:')
                    res.body = res.body.replace(/src="https:/g, 'src="'+ $.apiPath + 'img?img=https:')
                    this.data = res
                    window.scrollTo(0,0);
                })
            }
            catch(e){
                this.article = ''
            }
        }
    }
}
</script>

<style>

</style>
