import {authServices} from '../../services/authServices'
import router from '@/router'

const user = JSON.parse(localStorage.getItem('user'));
const state = user
    ? {status: {loggedIn: true}, user}
    : {status: {}, user: null};


const actions = {
    login({ commit}, {email, password}) {
        commit('loginRequest', email);
        authServices.login({email,password})
            .then(user => {
                commit('loginSuccess', user);
                router.push('/');
                // setTimeout(() => {
                //     // display success message after route change completes
                //     dispatch('alert/success', 'Registration successful', { root: true });
                // })
                },
                error => {
                    console.log('vao login fail');
                    commit('loginFailure', error);
                    // dispatch('alert/error', error, {root: true});
                }
            )
    },

    register({commit}, data) {
        commit('registerRequest');
        authServices.register(data)
            .then(
                () => {
                    commit('registerSuccess');
                    // router.push('/login');
                    // setTimeout(() => {
                        // display success message after route change completes
                        // dispatch('alert/success', 'Registration successful', { root: true });
                    // })
                },
                error => {
                    commit('registerFailure', error);
                    // dispatch('alert/error', error, { root: true });
                }
            );
    },

    logout({ commit }) {
        authServices.logout();
        commit('logout');
        router.push('/login')
    },
};

const mutations = {
    loginRequest(state, user) {
        state.status = {loggingIn: true};
        state.user = user;
    },
    loginSuccess(state, user) {
        state.status = {loggedIn: true};
        state.user = user;
    },
    loginFailure(state) {
        state.status = { loginFail: true};
        state.user = null;
    },
    logout(state) {
        state.status = {};
        state.user = null;
    },
    registerRequest(state) {
        state.status = { registering: true };
    },
    registerSuccess(state) {
        state.status = { registered: true};
    },
    registerFailure(state) {
        state.status = {};
    }
};

export default {
    namespaced: true,
    state,
    actions,
    mutations
}