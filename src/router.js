import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Lessons from '@/pages/Lessons'
import PageLesson from '@/pages/PageLesson';
import PageWord from '@/pages/PageWord';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: VueDemo
        },
        {
            path: '/messages',
            name: 'messages',
            component: Messages
        },
        {
            path: '/lessons',
            name: 'lessons',
            component: Lessons
        },
        {
            path: '/lessons/:id',
            name: 'wordinlesson',
            component: PageLesson
        },
        {
            path: '/word/:id',
            name: 'word',
            component: PageWord
        }
    ]
})
