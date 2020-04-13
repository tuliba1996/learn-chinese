import api from '@/services/api'

export default {
    login(payload) {
        return api.post(`token/`, payload)
            .then(response => response.data)
    },
}
