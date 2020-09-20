graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 16
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 157
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 67
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 57
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 134
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 174
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 102
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 152
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 61
  ]
]
