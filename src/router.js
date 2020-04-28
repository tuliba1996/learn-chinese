import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/pages/HomePage'
import Messages from '@/components/Messages'
import Lessons from '@/pages/Lessons'
import PageLesson from '@/pages/PageLesson';
import PageWord from '@/pages/PageWord';
import Login from '@/pages/auth/Login';
import Register from '@/pages/auth/Register';
import SearchWord from "./pages/SearchWord";

Vue.use(Router);

const router =  new Router({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: HomePage},
        { path: '/messages', name: 'messages', component: Messages},
        { path: '/lessons', name: 'lessons', component: Lessons},
        { path: '/lessons/:id', name: 'wordinlesson', component: PageLesson},
        { path: '/word/:id', name: 'word', component: PageWord},
        { path: '/register', name: 'register', component: Register},
        { path: '/search', name: 'search', component: SearchWord},
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
