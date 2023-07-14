from app.receiver.receiver import receiver


if __name__ == "__main__":
  try:
    receiver()
  except KeyboardInterrupt:
    print('Interrupted')