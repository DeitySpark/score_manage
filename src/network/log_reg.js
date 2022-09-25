import { request } from '@/network/request'
import qs from 'qs'

export function loginSub(data) {
  return request({
    url: '/user/login',
    method: 'POST',
    data: qs.stringify(data)
  })
}

export function registerSub(data) {
  return request({
    url: '/user/register',
    method: 'POST',
    data: qs.stringify(data)
  })
}
