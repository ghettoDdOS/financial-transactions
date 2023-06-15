import type {
  ObtainTokenRequest,
  ObtainTokenResponse,
  User,
  UserCreateRequest,
  TokenVerifyRequest
} from '@/models/auth'

import { api } from '@/plugins/axios'

export default {
  _endpoint: 'auth/',

  token(data: ObtainTokenRequest) {
    return api.post<ObtainTokenResponse>(`${this._endpoint}token/`, data)
  },
  verify(data: TokenVerifyRequest) {
    return api.post<{}>(`${this._endpoint}token/verify/`, data)
  },
  userCreate(data: UserCreateRequest) {
    return api.post<User>(`${this._endpoint}user/`, data)
  }
}
