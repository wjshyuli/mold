export function downloadBlob(data: BlobPart, filename: string) {
  const blob = new Blob([data])

  const url = window.URL.createObjectURL(blob)

  const a = document.createElement("a")
  a.href = url
  a.download = filename
  a.click()

  window.URL.revokeObjectURL(url)
}