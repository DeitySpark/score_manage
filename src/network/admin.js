import { request } from './request.js'
import qs from 'qs'

// 获取管理员信息
export function getTeacherInfo(data) {
  return request({
    url: '/student/get',
    method: 'POST',
    data: qs.stringify(data)
  })
}

// 学生成绩管理
export function getCourse(data) {
  return request({
    url: '/student/getStudentScore',
    method: 'GET',
    data: qs.stringify(data)
  })
}

