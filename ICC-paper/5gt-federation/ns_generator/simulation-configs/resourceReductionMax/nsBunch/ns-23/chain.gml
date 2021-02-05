graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 15
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 14
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 11
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 4
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 128
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 173
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 165
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 199
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 135
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 152
  ]
]
