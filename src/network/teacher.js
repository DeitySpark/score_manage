import { request } from './request.js'
import qs from 'qs'

// 获取教师信息
export function getTeacherInfo(data) {
  return request({
    url: '/teacher/get',
    method: 'POST',
    data: qs.stringify(data)
  })
}

// 课程管理
export function getStudentCourse(data) {
  return request({
    url: '/course/getcourse',
    method: 'POST',
    data: qs.stringify(data)
  })
}

