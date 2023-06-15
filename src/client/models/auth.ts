export interface ObtainTokenRequest {
  email: string
  password: string
}

export type JWTToken = string

export interface ObtainTokenResponse {
  access: JWTToken
}

export interface TokenVerifyRequest {
  token: JWTToken
}

export interface User {
  readonly id: number
  firstName: string
  lastName: string
  email: string
}

export interface UserCreateRequest extends Omit<User, 'id'> {
  password: string
  passwordConfirm: string
}
