import numpy as np

def conv_naive(x, out_c, ksize, padding = 0, stride = 1):
    b, in_c, h, w = x.shape
    kernel = np.random.rand( in_c, out_c, ksize, ksize)
    if padding > 0:
        pad_x = np.zeros((b, in_c, h+2*padding, w+2*padding))
        pad_x[:,:,padding:-padding,padding:-padding] = x
    out_h = (h + 2*padding - ksize)//stride + 1
    out_w = (w + 2*padding - ksize)//stride + 1
    out = np.zeros((b, out_c, out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            roi_x = pad_x[:, :, i*stride:i*stride+ksize, j*stride:j*stride+ksize]
            conv = np.tile(np.expand_dims(roi_x,2), (1,1,out_c,1,1))*kernel
            out[:,:,i,j] = np.sum(conv, axis = (1,3,4))
            # out[:,:,i,j] = np.squeeze(np.sum(conv, axis = (1,3,4), keepdims= True), axis = 3)
    return out

if __name__ == '__main__':
    x = np.random.rand(1,3,10,10)
    out = conv_naive(x, 15, ksize=3, padding=1, stride=2)
    print(out.shape)