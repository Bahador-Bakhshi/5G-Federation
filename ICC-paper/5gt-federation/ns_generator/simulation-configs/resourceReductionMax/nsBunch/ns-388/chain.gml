graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 3
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 160
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 134
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 188
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 61
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 179
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 200
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 101
  ]
]
