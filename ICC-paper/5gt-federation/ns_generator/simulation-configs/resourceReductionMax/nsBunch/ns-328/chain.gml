graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 9
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 79
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 70
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 50
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 184
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 163
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 109
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 195
  ]
]
