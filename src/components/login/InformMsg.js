/* eslint-disable */
import { ElMessage} from "element-plus";

const msg = (fun, message) => {
  if (fun === 'message') {
    message(message)
  } else if (fun === 'success') {
    success(message)
  } else if (fun === 'warning') {
    warning(message)
  } else if (fun === 'error') {
    error(message)
  }
}
const message = (message) => {
  ElMessage({
    showClose: true,
    message: message,
    type: 'message',
  })
}

const success = (message) => {
  ElMessage({
    showClose: true,
    message: message,
    type: 'success',
  })
}
const warning = (message) => {
  ElMessage({
    showClose: true,
    message: message,
    type: 'warning',
  })
}
const error = (message) => {
  ElMessage({
    showClose: true,
    message: message,
    type: 'error',
  })
}

export { msg }
