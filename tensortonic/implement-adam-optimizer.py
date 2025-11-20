import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    m_curr = beta1 * m + (1 - beta1) * grad 
    v_curr = beta2 * v + (1 - beta2) * (grad * grad) 

    m_new = m_curr / (1 - beta1**t )
    v_new = v_curr / (1 - beta2**t)

    param_new = param - lr * (m_new / (np.sqrt(v_new) + eps))

    return (param_new,m_curr,v_curr) 
