graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 1
    memory 5
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 85
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 128
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 57
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 74
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 61
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 166
  ]
]
