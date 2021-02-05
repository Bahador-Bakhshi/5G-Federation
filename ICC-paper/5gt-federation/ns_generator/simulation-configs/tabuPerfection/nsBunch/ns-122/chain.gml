graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 4
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 5
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 16
  ]
  node [
    id 5
    label 6
    disk 10
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
    bw 152
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 71
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 161
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 53
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 78
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 138
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 109
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 63
  ]
]
