import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Lessons from '@/pages/Lessons'
import PageLesson from '@/pages/PageLesson';
import PageWord from '@/pages/PageWord';
import Login from '@/pages/auth/Login';

Vue.use(Router);

const router =  new Router({
    // mode: 'history',
    routes: [
        { path: '/', name: 'home', component: VueDemo},
        { path: '/messages', name: 'messages', component: Messages},
        { path: '/lessons', name: 'lessons', component: Lessons},
        { path: '/lessons/:id', name: 'wordinlesson', component: PageLesson},
        { path: '/word/:id', name: 'word', component: PageWord},
        { path: '/login', name: 'login', component:  Login},
        // otherwise redirect to home
        { path: '*', redirect: '/' }
    ]
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/register'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next('/login');
  }
  next();
})

export default router;
