import torch
import torch.nn as nn
import binvox_rw
import torch.utils.data as data

from dataset import BinvoxDataset


class BinvoxMLModel(nn.Module):

    DIM = 256

    def __init__(self):
        super(BinvoxMLModel, self).__init__()
        # replace with your desired model architecture
        self.seq = nn.Sequential(
            nn.Flatten(),
            nn.LazyLinear(1)
        )

    def forward(self, x):
        x = x.float()  # convert voxel boolean array to float
        x = self.seq(x)
        return x

# source: https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html


def training_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        pred = model(X.float())
        loss = loss_fn(pred, y.float())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 1 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

# source: https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html


def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    print(num_batches)
    test_loss = 0

    max_iter = 1

    with torch.no_grad():
        for i, (X, y) in enumerate(dataloader):
            pred = model(X.float())
            print(i)
            test_loss += loss_fn(pred, y.float())
            if i > max_iter:
                break

    test_loss /= min(max_iter, num_batches)
    print(f"Test Error: \n Avg loss: {test_loss:>8f} \n")


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using {device} device")

    model = BinvoxMLModel().to(device)
    print(model)

    dataset = BinvoxDataset('data/rating_data.csv', 'data/id_data.csv')

    sampler = data.BatchSampler(data.RandomSampler(
        dataset), batch_size=1, drop_last=False)
    loader = data.DataLoader(dataset, batch_sampler=sampler)

    training_loop(loader, model, nn.MSELoss(),
                  torch.optim.Adam(model.parameters(), lr=0.001))
