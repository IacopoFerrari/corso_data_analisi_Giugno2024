# il prodotto di due matrici:
A = np.random.rand(4,5)  # matrice a valori pseudo-casuali
B = np.random.rand(5,2)  # matrice a valori pseudo-casuali
pr_gemm_1 = A @ B 

# vediamo l'algoritmo nel dettaglio di un'implementazione scalare:
pr_gemm_2 = np.zeros((A.shape[0],B.shape[1]))
for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            pr_gemm_2[i,j] += A[i,k] * B[k,j]
        #endfor
    #endfor
#endfor

# confronto:
print("np.sum(np.sum(np.abs(pr_gemm_1-pr_gemm_2))) = ",np.sum(np.sum(np.abs(pr_gemm_1-pr_gemm_2))))