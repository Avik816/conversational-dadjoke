# This repo holds the files for a local conversational Dad Joke AI with a web-based chat UI powered by vector embeddings and semantic retrieval.

# This project is a work in progress 🔃


# Notes (temp):
## Kmeans formula to use for n.o. clusters:
We estimate the optimal number of clusters using the Kmeans heuristic:

$$
k \approx \sqrt{\frac{N}{2}} \Rightarrow \sqrt{\frac{43000}{2}} \approx \sqrt{21500} \approx 146 \text{ clusters.}
$$


## Imp:
faiss-gpu/faiss-cpu

depends on the system architecture of the user, the following are the requirements for gpu version:
- Requires PyTorch + CUDA already installed.
- Windows GPU support is less stable (better on Linux).
- You may hit dependency issues if CUDA versions mismatch.
