# Project EL

The Chance of getting ALL7 (6 numbers + 1 bonus ball) is: **1 in 2,658,391,066**

## Training The Model

```python
def train_model(model, epochs=10, batch_size=32, graph=False):
    x_train, x_ro_train, y_train = load_data_and_labels()

    # Train the model
    hist = model.fit([x_train, x_ro_train],
                     y_train,
                     epochs,
                     batch_size,
                     validation_split=0.08,
                     callbacks=[checkpoint, callback, cooldown]
                     )
```

The incredible size of all the combinations and the computational power required is beyond my current capabilities. While I can develop the software, I lack the necessary hardware. I am working with an i7 laptop and 42 GB of RAM, but to train this model on every possible combination would take an unimaginable amount of time, far beyond a human lifetime. This project has great potential, and with proper funding, it could achieve extraordinary results.

These models can improve significantly, and my goal is to reach absolute accuracy, 100%. However, to achieve this, I need support. This is one reason I am sharing this project — to demonstrate its potential and appeal for investment.

### Provided Resources

Here, you will find a synthetic dataset (Superset) that was used to train the model. This dataset is provided to help others understand the methodology and potential of the project.

The Supersets are the key to the effect.

---

### Understanding Lottery Odds

#### Basics of Probability

Probability measures the likelihood that an event will occur. For the lottery, this means calculating how likely it is to pick the correct numbers out of a possible set.

#### Simple Example with 2 Numbers

Let’s start with a simple lottery where you need to pick 2 numbers, each ranging from 1 to 59:

- **Total combinations**: To find out how many different combinations of 2 numbers you can pick from 59, you use the combination formula:

  \[
  C(59, 2) = \frac{59!}{2!(59-2)!} = 1711
  \]

  So, there are 1,711 possible combinations when picking 2 numbers from 59.

#### Increasing to 3 Numbers

Now, if the lottery requires you to pick 3 numbers:

  \[
  C(59, 3) = \frac{59!}{3!(59-3)!} = 32,737
  \]

  So, there are 32,737 possible combinations when picking 3 numbers from 59.

#### Standard Lottery (6 Numbers)

In a standard lottery, you need to pick 6 numbers out of 59:

  \[
  C(59, 6) = \frac{59!}{6!(59-6)!} = 45,057,474
  \]

  So, there are 45,057,474 possible combinations when picking 6 numbers from 59.

#### Adding a Bonus Ball

If the lottery also includes a bonus ball, which is another number from 1 to 59, the total number of combinations increases further. Assuming the bonus ball is an additional, separate draw:

- **Combinations with 6 numbers**: 45,057,474
- **Bonus ball choices**: 59

  So, the total number of combinations including the bonus ball is:

  \[
  45,057,474 \times 59 = 2,658,391,066
  \]

  This means there are 2,658,391,066 possible combinations when picking 6 numbers and an additional bonus ball from 1 to 59.

### Explaining the Increasing Odds

As you add more numbers to pick from or additional draws (like a bonus ball), the total number of possible combinations increases significantly. This makes it much harder to predict all the correct numbers.

- **2 numbers**: 1 in 1,711
- **3 numbers**: 1 in 32,737
- **6 numbers**: 1 in 45,057,474
- **7 numbers (6 numbers + 1 bonus ball)**: 1 in 2,658,391,066

### Conclusion

To win a lottery with 6 numbers and a bonus ball, you need to predict a combination out of over 2.6 billion possibilities. As you can see, the odds of winning increase dramatically with each additional number or condition added to the lottery, highlighting the extreme unlikelihood of winning such lotteries.

### A Call for Support

I have reached the maximum capacity of my system, and to take this project to the next level, I need your help. Investing in this project could lead to groundbreaking results, and I am offering parts of the project for free to demonstrate its potential. With proper funding, we can improve these models and possibly achieve 100% accuracy.

As someone with limited financial resources, I am appealing to you to support this project. Whether through donations, hardware contributions, or sharing this project with others, any help would be greatly appreciated. Together, we can turn this ambitious project into a reality.

Thank you for your time and consideration.

---

### Current and Future Value

It may not be obvious to you how good this is, but in science, they use sigma to determine if an effect is true. Here are the current and future projections for the project:

#### NOW:
- **Current Value**: The project has a significant value now, given its current state and the potential it demonstrates.

#### Future:
- **Future Value**: It took over 3 years to get this far on my own. If I were to improve it by 20-30% more, it could generate a reasonable permanent income.
- **Potential**: If perfected, this could be the most valuable software ever written.

Your support can help realize this potential, making significant strides in the development and application of this model.

