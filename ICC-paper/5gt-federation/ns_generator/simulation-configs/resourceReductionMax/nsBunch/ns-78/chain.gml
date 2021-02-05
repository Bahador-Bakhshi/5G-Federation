graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 5
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 114
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 156
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 188
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 118
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 169
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 101
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 179
  ]
]
