import { request } from '@/network/request'
import qs from 'qs'

export function loginSub(data) {
  return request({
    url: '/account/login',
    method: 'POST',
    data: qs.stringify(data)
  })
}

export function registerSub(data) {
  return request({
    url: '/account/register',
    method: 'POST',
    data: qs.stringify(data)
  })
}
