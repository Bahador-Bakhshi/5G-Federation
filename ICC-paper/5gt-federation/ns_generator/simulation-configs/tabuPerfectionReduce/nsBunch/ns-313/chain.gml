graph [
  node [
    id 0
    label 1
    disk 8
    cpu 3
    memory 9
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 16
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 159
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 152
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 162
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 140
  ]
  edge [
    source 1
    target 5
    delay 28
    bw 79
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 189
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 61
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 63
  ]
]
