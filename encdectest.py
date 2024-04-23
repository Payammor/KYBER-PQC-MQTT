import timeit
import psutil
from implement import (
    generate_keypair_768,
    encrypt_768,
    decrypt_768,
    CRYPTO_PUBLICKEYBYTES_768,
    CRYPTO_SECRETKEYBYTES_768,
    CRYPTO_CIPHERTEXTBYTES_768,
    CRYPTO_BYTES_768
)

def measure_cpu_usage(func, *args, **kwargs):
    """ Function to measure CPU usage while running the provided function """
    psutil.cpu_percent()  # call to start measuring
    start_time = timeit.default_timer()
    result = func(*args, **kwargs)
    elapsed_time = timeit.default_timer() - start_time
    cpu_usage = psutil.cpu_percent()  # get CPU usage after operation
    return result, elapsed_time, cpu_usage

def test_keypair_generation(iterations=10):
    for _ in range(iterations):
        public_key, private_key = generate_keypair_768()
        assert len(public_key) == CRYPTO_PUBLICKEYBYTES_768
        assert len(private_key) == CRYPTO_SECRETKEYBYTES_768
    print("Keypair generation test passed!")

def test_encryption_decryption(iterations=10):
    total_encryption_time = 0
    total_decryption_time = 0
    avg_encryption_cpu = 0
    avg_decryption_cpu = 0

    for _ in range(iterations):
        public_key, private_key = generate_keypair_768()

        # Encrypt a message using the public key
        (ciphertext, shared_secret_enc), enc_time, enc_cpu = measure_cpu_usage(encrypt_768, public_key)
        total_encryption_time += enc_time
        avg_encryption_cpu += enc_cpu

        assert len(ciphertext) == CRYPTO_CIPHERTEXTBYTES_768
        assert len(shared_secret_enc) == CRYPTO_BYTES_768

        # Decrypt the message using the private key
        shared_secret_dec, dec_time, dec_cpu = measure_cpu_usage(decrypt_768, ciphertext, private_key)
        total_decryption_time += dec_time
        avg_decryption_cpu += dec_cpu

        assert shared_secret_enc == shared_secret_dec

    print("Encryption and decryption tests passed!")
    print(f"Average Encryption Time: {total_encryption_time/iterations}s, Average Decryption Time: {total_decryption_time/iterations}s")
    print(f"Average Encryption CPU Usage: {avg_encryption_cpu/iterations}%, Average Decryption CPU Usage: {avg_decryption_cpu/iterations}%")

# Run the tests
test_keypair_generation()
test_encryption_decryption()
