# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I75eBrYE5HcfQ9xg-_-G-t7_eOoKrQZQ
"""

def jaccard_similarity(file1,file2):
  set1 = set(file1.split())
  set2 = set(file2.split())

  intersection = set1.intersection(set2)
  union = set1.union(set2)

  similarity = len(intersection) / len(union)

  return similarity, intersection

file1= "History is the systematic study of the past"
file2= "History is the systematic study of the past this is just for practice"

similarity, common_words = jaccard_similarity(file1, file2)

print(f"Similarity: {similarity:.2f}")
print(f"Common words: {common_words}")