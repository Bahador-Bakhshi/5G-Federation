graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 3
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 2
    memory 1
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 183
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 113
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 99
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 178
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 91
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 160
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 110
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 128
  ]
]
