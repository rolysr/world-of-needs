import statistics as st
from scipy.stats import normaltest
import numpy as np
import random as rd

def Metrics(distances):
    mean= st.mean(distances)
    variance= st.stdev(distances)
    mode=st.mode(distances)
    median=st.median(distances)
    print("Median: "+str(median))
    print("Mode: "+str(mode))
    print("Mean: "+ str(mean))
    print("Desviation: "+ str(variance))

distances= [133, 66, 138, 130, 99, 62, 65, 58, 74, 119, 146, 94, 135, 134, 72, 139, 110, 139, 78, 127, 85, 100, 100, 100, 100, 107, 95, 91, 107, 96, 98, 104, 100, 105, 90, 96, 105, 99, 106, 97, 106, 94, 103, 109, 96, 98, 109, 101, 109, 95, 106, 95, 102, 93, 108, 92, 99, 106, 94, 106, 99, 94, 101, 99, 102, 96, 97, 94, 106, 105, 106, 102, 98, 91, 103, 100, 100, 100, 107, 95, 91, 107, 96, 98, 104, 100, 105, 90, 96, 105, 99, 106, 97, 106, 94, 103, 109, 96, 98, 109, 101, 109, 95, 106, 95, 102, 93, 108, 92, 99, 106, 94, 106, 99, 94, 101, 99, 102, 96, 97, 94, 106, 105, 106, 102, 98, 91, 103, 100, 100, 100, 107, 95, 91, 107, 96, 98, 104, 100, 105, 90, 96, 105, 99, 106, 97, 106, 94, 103, 109, 96, 98, 109, 101, 109, 95, 106, 95, 102, 93, 108, 92, 99, 106, 94, 106, 99, 94, 101, 99, 102, 96, 97, 94, 106, 105, 106, 102, 98, 91, 103, 100, 101, 99, 100, 107, 100, 107, 95, 91, 107, 96, 98, 104, 100, 105, 90, 96, 105, 99, 106, 97, 106, 94, 103, 109, 96, 98, 109, 101, 109, 95, 106, 95, 102, 93, 108, 92, 99, 106, 94, 106, 99, 94, 101, 99, 102, 96, 97, 94, 106, 105, 106, 102, 98, 91, 103, 101, 99, 100, 107, 100, 100, 100, 101, 99, 100, 107, 100, 100, 101, 99, 100, 107, 100, 100, 101, 99, 100, 107, 100, 100, 100, 100, 101, 99, 100, 107, 100, 100, 98, 97, 93, 89, 88, 105, 100, 100, 101, 99, 100, 107, 100, 100, 100, 101, 99, 100, 107, 100, 100, 100, 94, 84, 137, 75, 93, 134, 109, 51, 125, 99, 24, 102, 40, 101, 87, 99, 146, 104,  40, 73, 75, 93, 32, 32, 112, 114, 42, 91, 103, 128, 54, 164, 36, 31, 87, 25, 97, 140, 99, 112, 79, 148, 27, 66,92, 48, 113, 61, 89, 68, 49, 89, 102, 152, 94, 80, 113, 155, 158, 172, 149, 61, 130, 47, 53, 60, 74, 69, 146, 128, 101, 99, 100, 107, 121, 57, 119, 71, 37, 61, 66, 74, 104, 100, 22, 139, 98, 66, 110, 99, 116, 97, 110, 119, 86, 115, 106, 106, 91, 141, 54, 140, 57, 113, 85, 97, 135, 127, 152, 136, 126, 98, 59, 80, 124, 97, 95, 121, 121, 99, 84,  71, 136, 126, 116, 45, 127, 94, 110, 101, 99, 100, 85, 110, 46, 75, 62, 127, 131, 94, 114, 80, 118, 140, 59, 126, 118, 147, 81, 36, 101, 99, 100, 129, 74, 123,  55, 53, 67, 112, 85, 76, 175, 100, 167, 99, 73, 38, 41, 103, 143, 94, 169, 32, 86, 68, 49, 149, 59, 133, 54, 44, 133, 105, 27, 60, 142, 155, 89, 42, 28, 100, 100, 101, 99, 100, 107, 100, 100, 100, 101, 99, 100, 107, 100, 100, 148, 132, 166, 74, 136, 100, 152, 96, 125, 180, 123, 71, 42, 73, 22, 54, 146, 117, 94, 34, 70, 139, 94, 109, 128, 142, 132, 89, 46, 100, 40, 71, 78, 73, 21, 31, 26, 57, 140, 176, 112, 77, 116, 141, 144, 113, 93, 103, 65, 88, 74, 101, 99, 100, 42, 112, 135, 54, 60, 129, 114, 60, 108, 57, 138, 59, 72, 111, 72, 89, 48, 147, 85, 97, 69, 154, 174, 88, 69, 68, 129, 148, 60, 59, 100,79, 140, 101, 99, 100, 94, 58, 59, 109, 57, 144, 97, 120, 73, 63, 100, 55, 121, 100, 140, 98, 151, 134, 63, 83, 132, 175, 117, 116, 109, 85, 124, 52, 100, 101, 99, 127, 152, 66, 106, 101, 99, 100, 76, 70, 96, 101, 150, 113, 116, 37, 44, 110, 43, 113, 103, 89, 50, 132, 170, 110, 175, 83, 77, 81, 138, 72, 51, 91, 91, 59, 76, 123, 155, 139, 93, 63, 150, 180, 162, 149, 122, 161, 99, 70, 35, 72, 116, 101, 99, 100, 150, 180, 144, 170, 57, 35, 79, 62, 21, 40, 40, 80, 115, 122, 41, 163, 118, 57, 57, 73, 78, 70, 175, 22, 171, 84, 157, 80, 125, 39, 104, 126, 157, 89, 23, 79, 137, 79, 76, 147, 34, 27, 65, 65, 34, 46, 121, 113, 27, 29, 64, 179, 84, 131, 106, 68, 54, 172, 168, 97, 61, 131, 44, 172, 111, 112, 180, 109, 154, 100, 162, 58, 156, 143, 21, 103, 101, 99, 100, 56, 90, 116, 41, 37, 145, 70, 94, 70, 101, 99, 100, 41, 67, 144, 154, 24, 91, 168, 74, 94, 49, 152, 100, 109, 46, 163, 121, 33, 164, 169, 100, 100,146, 141, 48, 53, 125, 71, 151, 63, 133, 129, 134, 139, 110, 101, 105, 103, 83, 86, 148, 77, 70, 88, 152, 101, 99, 100, 115, 76, 43, 140, 120, 143, 124, 101, 99, 100, 151, 56, 100, 100, 100, 100, 75, 167, 112, 89, 41, 72, 48, 175, 109, 66, 169, 139, 32, 100, 100, 100, 100, 24, 126, 162, 170, 42, 152, 121, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 105, 101, 99, 100, 67, 130, 28, 169, 135, 37, 171, 101, 99, 100, 149, 72, 21, 48, 177, 62, 155, 179, 62, 40, 67, 117, 23, 125, 101, 99, 100, 142, 42, 20, 72, 52, 163, 61, 112, 71, 56, 176, 83, 79, 44, 155, 115, 41, 173, 82, 109, 169, 139, 78, 40, 172, 116, 26, 131, 152, 164, 94, 89, 78, 77, 100, 100, 100, 135, 58, 96, 76, 71, 116, 62, 90,  36, 142, 95, 48, 55, 105, 110, 52, 51, 97, 129, 52, 44, 118, 144, 124, 36, 142, 40, 37, 99, 132, 97, 129, 140, 87, 85, 146, 93, 28, 76, 63, 70, 67, 77, 70, 103, 74, 166, 156, 81, 112, 168, 43, 109, 115, 112, 146, 38, 77, 83, 123, 125, 129, 51, 75, 128, 91, 55, 65, 52, 47, 103, 31, 89, 129, 71, 45, 153, 59, 86, 85, 80, 110, 108, 91, 114, 159, 86, 120, 34, 84, 137, 82, 162, 72, 173, 135, 110, 57, 70, 39, 50, 39, 176, 118, 106, 128, 88, 104, 122, 126, 129, 45, 138, 38, 136, 81, 133, 133, 51, 75, 127, 29, 174, 71, 159, 114, 102, 136, 116, 40, 144, 90, 85, 112, 87, 132, 127, 75, 84, 122, 63, 96, 78, 90, 113, 92, 102, 155, 81, 100, 125, 53, 66, 88, 100, 116, 78, 117, 75, 124, 77, 86, 69, 130, 119, 81, 73, 138, 148, 145, 138, 52, 62, 126, 28, 112, 119, 57, 127, 71, 111, 58, 123, 125, 100]

stat,p = normaltest(distances)
alpha=0.5
if p > alpha:
    print("La muestra parece gaussiana")
else:
    print("La muestra no parece  Gaussian")


