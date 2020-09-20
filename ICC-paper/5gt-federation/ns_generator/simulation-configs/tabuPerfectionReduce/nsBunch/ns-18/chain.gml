graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 7
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 10
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
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
    bw 163
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 90
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 184
  ]
  edge [
    source 0
    target 3
    delay 29
    bw 60
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 105
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 84
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 172
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 77
  ]
]
